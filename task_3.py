import json
from typing import Any

from core.enums import TEST_DOC_PATH, INITIAL_TEST_DOC_PATH


def load_json() -> dict[str, Any]:
    with INITIAL_TEST_DOC_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data: dict[str, Any]) -> None:
    with TEST_DOC_PATH.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_new_document(data: dict[str, Any]) -> None:
    data["document4"] = {"1": {"parents": {"document3": ["3"]}}}


def remove_parent_references(
    data: dict[str, Any],
    parent_document: str,
    parent_version: str,
) -> list[tuple[str, str]]:
    versions_to_delete = []

    for document_name, versions in data.items():
        for version_number, version_data in versions.items():
            parents = version_data.get("parents", {})

            if parent_document not in parents:
                continue

            if parent_version in parents[parent_document]:
                parents[parent_document].remove(parent_version)

            if not parents[parent_document]:
                del parents[parent_document]

            if not parents:
                versions_to_delete.append((document_name, version_number))

    return versions_to_delete


def delete_version(
    data: dict[str, Any],
    document_name: str,
    version_number: str,
) -> None:
    if document_name not in data:
        return

    if version_number not in data[document_name]:
        return

    del data[document_name][version_number]

    child_versions = remove_parent_references(
        data=data,
        parent_document=document_name,
        parent_version=version_number,
    )

    for child_document, child_version in child_versions:
        delete_version(data, child_document, child_version)


def main() -> None:
    data = load_json()

    add_new_document(data)

    delete_version(
        data=data,
        document_name="document1",
        version_number="1",
    )

    save_json(data)


if __name__ == "__main__":
    main()
