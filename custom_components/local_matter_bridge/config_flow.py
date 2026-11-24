"""Config flow for Local Matter Bridge."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN, DEFAULT_NAME


class LocalMatterBridgeConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):
    """Handle config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle initial setup."""

        if user_input is not None:
            await self.async_set_unique_id(DOMAIN)
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=user_input["name"],
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(
                    "name",
                    default=DEFAULT_NAME,
                ): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )

