# HA Local Matter Bridge Architecture

## Overview

Convert Home Assistant entities into Matter bridge endpoints.

## Flow

Home Assistant Entity
        ↓
Local Matter Bridge
        ↓
Matter Endpoint
        ↓
Matter Controller

Examples:

- Alexa
- Apple Home
- Google Home
- SmartThings

## Supported Domains

Phase 1

- light
- switch

Phase 2

- fan
- cover
- lock

Phase 3

- scenes
- scripts
- helpers
