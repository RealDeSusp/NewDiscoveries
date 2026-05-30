from typing import Any

import requests
from requests import HTTPError

from core.enums import BASE_URL


def call_api(
    method: str,
    url: str,
    body: dict | None = None,
) -> dict[str, Any] | None:
    response = requests.request(
        method=method,
        url=url,
        json=body,
        timeout=10,
    )
    response.raise_for_status()

    if response.status_code == 204:
        return None

    return response.json()


def run_api_flow() -> None:
    create_request_body = {
        "name": "Test object",
        "data": {"first_attribute": "some string", "second_attribute": 1345},
    }
    created_object = call_api("POST", BASE_URL, create_request_body)
    if not created_object or "id" not in created_object:
        raise ValueError(f"Объект не создан или нет id: {created_object}")
    print("Создан объект:\n", created_object, sep="")

    created_id = created_object["id"]
    object_url = f"{BASE_URL}/{created_id}"
    try:
        received_object = call_api("GET", object_url)
        print("Получен объект:\n", received_object, sep="")
    except HTTPError as e:
        print("Не удалось получить объект:", e)
        print("Продолжаем: пробуем PATCH и DELETE")

    patch_request_body = {
        "name": "Changed test object",
    }
    try:
        updated_object = call_api("PATCH", object_url, patch_request_body)
        print("Обновлён объект:\n", updated_object, sep="")
    except HTTPError as e:
        print("Не удалось обновить объект:", e)
        return

    try:
        delete_result = call_api("DELETE", object_url)
        print("Объект удалён:", delete_result)
    except HTTPError as e:
        print("Не удалось удалить объект:", e)
        return
    try:
        call_api("GET", object_url)
    except HTTPError as e:
        print(
            "Попытка получить удалённый объект завершилась с 404 ошибкой:",
            e,
            "\nЭто ожидаемое поведение",
        )


if __name__ == "__main__":
    run_api_flow()
