"""Persistent storage."""

from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store

from .const import (
    STORAGE_KEY,
    STORAGE_VERSION,
)


class LocalMatterBridgeStorage:
    """Storage manager."""

    def __init__(
        self,
        hass: HomeAssistant,
    ) -> None:

        self._store = Store(
            hass,
            STORAGE_VERSION,
            STORAGE_KEY,
        )

    async def async_load(self):

        data = await self._store.async_load()

        if data is None:
            return {
                "entities": []
            }

        return data

    async def async_save(
        self,
        data,
    ):

        await self._store.async_save(data)
