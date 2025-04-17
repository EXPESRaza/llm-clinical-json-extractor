import json
import jsonschema

llm_response_schema = {
    "type": "object",
    "properties": {
        "device": {"type": "string"},
        "mask_type": {"type": "string"},
        "add_ons": {"type": "array", "items": {"type": "string"}},
        "qualifier": {"type": "string"},
        "ordering_provider": {"type": "string"},
        "diagnosis": {"type": "string"},
        "SpO2": {"type": "string"},
        "usage": {"type": "array", "items": {"type": "string"}},
        "type": {"type": "string"},
        "features": {"type": "array", "items": {"type": "string"}},
        "mobility_status": {"type": "string"},
        "product": {"type": "string"},
        "components": {"type": "array", "items": {"type": "string"}},
        "compliance_status": {"type": "string"}
    },
    "required": ["device", "ordering_provider"],
    "additionalProperties": False
}

def validate_response(response_json: str, schema: dict):
    try:
        data = json.loads(response_json)
        jsonschema.validate(instance=data, schema=schema)
        return True, None
    except jsonschema.ValidationError as e:
        return False, str(e)
    except json.JSONDecodeError:
        return False, "Invalid JSON format"