from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
OVERVIEW_DIR = REPO_ROOT / "public" / "00_AI知识总览"
NODES_DIR = OVERVIEW_DIR / "nodes"
OUTPUT_PATH = OVERVIEW_DIR / "node-data.json"
EXCLUDED_FILENAMES = {"README.md", "TEMPLATE.md"}


def split_front_matter(raw: str) -> tuple[str, str]:

    if not raw.startswith("---"):
        return "", raw.strip()

    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        return "", raw.strip()

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            front = "\n".join(lines[1:index])
            body = "\n".join(lines[index + 1 :]).strip()
            return front, body

    return "", raw.strip()


def parse_front_matter(text: str) -> dict[str, Any]:
    result: dict[str, Any] = {
        "tags": [],
        "related": [],
        "sources": [],
    }
    if not text.strip():
        return result

    current_key = ""
    current_source: dict[str, str] | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue

        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if key_match and not line.startswith("  "):
            current_key = key_match.group(1)
            value = key_match.group(2).strip()
            current_source = None
            if current_key in {"tags", "related", "sources"}:
                if value and current_key != "sources":
                    result[current_key].append(value)
                elif current_key == "sources" and value:
                    result[current_key].append({"name": value})
            else:
                result[current_key] = value
            continue

        item_match = re.match(r"^\s*-\s*(.*)$", line)
        if item_match:
            value = item_match.group(1).strip()
            if current_key in {"tags", "related"}:
                if value:
                    result[current_key].append(value)
                continue
            if current_key == "sources":
                current_source = {}
                name_match = re.match(r"^name:\s*(.*)$", value)
                if name_match:
                    current_source["name"] = name_match.group(1).strip()
                elif value:
                    current_source["name"] = value
                result[current_key].append(current_source)
                continue

        if current_key == "sources" and current_source is not None:
            source_match = re.match(r"^\s+([A-Za-z0-9_-]+):\s*(.*)$", line)
            if source_match:
                current_source[source_match.group(1)] = source_match.group(2).strip()

    return result


def parse_sections(body: str) -> list[dict[str, str]]:
    matches = list(re.finditer(r"^##\s+(.+)$", body, re.MULTILINE))
    if not matches:
        return []

    sections: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        content = body[start:end].strip()
        if content:
            sections.append({"title": title, "content": content})
    return sections


def get_summary(sections: list[dict[str, str]], body: str) -> str:
    source_text = sections[0]["content"] if sections else body
    for block in re.split(r"\n\s*\n", source_text):
        cleaned = re.sub(r"\s+", " ", block).strip()
        if cleaned:
            return cleaned
    return ""


def build_node_payload(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    front_text, body = split_front_matter(raw)
    front = parse_front_matter(front_text)
    sections = parse_sections(body)
    node_id = front.get("id") or path.stem

    payload: dict[str, Any] = {
        "id": node_id,
        "title": front.get("title") or node_id,
        "type": front.get("type") or "",
        "category": front.get("category") or "",
        "provider": front.get("provider") or "",
        "status": front.get("status") or "",
        "visibility": front.get("visibility") or "",
        "confidence": front.get("confidence") or "",
        "updated": front.get("updated") or "",
        "tags": front.get("tags") or [],
        "sources": front.get("sources") or [],
        "related": front.get("related") or [],
        "summary": get_summary(sections, body),
        "sections": sections,
        "sourcePath": path.relative_to(OVERVIEW_DIR).as_posix(),
    }
    return payload


def main() -> None:
    nodes: dict[str, Any] = {}
    files = sorted(
        file_path
        for file_path in NODES_DIR.rglob("*.md")
        if file_path.name not in EXCLUDED_FILENAMES
    )

    for file_path in files:
        payload = build_node_payload(file_path)
        nodes[payload["id"]] = payload


    document = {
        "meta": {
            "title": "AI知识总览节点数据",
            "generatedFrom": "nodes/**/*.md",
            "nodeCount": len(nodes),
        },
        "nodes": nodes,
    }

    OUTPUT_PATH.write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"generated {OUTPUT_PATH} with {len(nodes)} nodes")


if __name__ == "__main__":
    main()
