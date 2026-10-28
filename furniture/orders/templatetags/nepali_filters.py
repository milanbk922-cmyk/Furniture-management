from django import template

register = template.Library()

@register.filter
def nepali_comma(value):
    try:
        number = str(int(value))
        last_three = number[-3:]
        remaining = number[:-3]

        if remaining:
            parts = []
            while remaining:
                parts.insert(0, remaining[-2:])
                remaining = remaining[:-2]

            return ",".join(parts) + "," + last_three

        return last_three

    except (ValueError, TypeError):
        return value