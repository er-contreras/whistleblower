import json
from openai import OpenAI
from django.conf import settings

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=settings.GROQ_API_KEY
)

def generate_incident_report(victim_name, classification):
    """
    LLama a la IA de Groq para generar el JSON estructurado.
    """

    prompt = f"""
    Generate a realistic whistleblower report in JSON format.
    Victim: {victim_name}
    Classification: {classification}

    The response MUST be only valid JSON following this exact structure:
    {{
        "date": "2026-01-01 15:00:00",
        "anonymous": true,
        "channel": "web",
        "reporter": {{ "reletionship_to_company": "employee", "country": "Mexico" }},
        "people": {{ "offender": {{ "name": "{victim_name}", "position": "Manager", "department": "Sales" }} }},
        "incident": {{
            "type": "{classification}", "description": "Resumen generado por Ai ...", "approximate_date": "2025-12", "is_going": true 
        }},
        "location": {{ "city": "CDMX", "work_related": true }},
        "evidence": {{ "has_evidence": true,  "description": "Capturas de pantalla adjuntas." }}
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente legal.\
                            Debes responder UNICAMENTE en formato JSON plano, sin bloques de codigo markdown ni texto adicional."
            },
            {
                "role": "user", "content": prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content
    print(f"Hello there {content}")
    return json.loads(content)
