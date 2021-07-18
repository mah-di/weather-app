from django import template



register = template.Library()


@register.filter
def wind_speed(x):
    if x == 'N/A':
        return x

    return "{:.2f}".format((x * 3600)/1000) + ' k/h'


@register.filter
def wind_direction(deg):
    if deg > 345 or deg <= 15:
        return f'N ({deg}°)'
    elif deg > 325:
        return f'N/NW ({deg}°)'
    elif deg > 305:
        return f'NW ({deg}°)'
    elif deg > 285:
        return f'W/NW ({deg}°)'
    elif deg > 255:
        return f'W ({deg}°)'
    elif deg > 235:
        return f'W/SW ({deg}°)'
    elif deg > 215:
        return f'SW ({deg}°)'
    elif deg > 195:
        return f'S/SW ({deg}°)'
    elif deg > 165:
        return f'S ({deg}°)'
    elif deg > 145:
        return f'S/SE ({deg}°)'
    elif deg > 125:
        return f'SE ({deg}°)'
    elif deg > 105:
        return f'E/SE ({deg}°)'
    elif deg > 75:
        return f'E ({deg}°)'
    elif deg > 55:
        return f'E/NE ({deg}°)'
    elif deg > 35:
        return f'NE ({deg}°)'
    elif deg > 15:
        return f'N/NE ({deg}°)'
    else:
        return 'N/A'

    
@register.filter
def visibility(m):
    return "{:.2f}".format(m/1000)