from urllib.parse import quote


def social_text(request):
    text = (
        "Assalomu Aleykum Sardorxon.\n"
        "Men sizni web sahifangizni kuzatdim va sizga taklifim bor edi.\n"
    )

    encoded = quote(text)

    return {
        "SOCIAL_TEXT": encoded,
        "SOCIAL_TEXT_RAW": text,
    }
