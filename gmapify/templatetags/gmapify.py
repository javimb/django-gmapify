from django import template


register = template.Library()


@register.inclusion_tag('gmapify/map.html')
def gmapify(html_id, lat, lng, **kwargs):
    """
    {% gmapify <html_id> <lat> <lng> [zoom=<zoom>] [map_type=<map_type>]
    [marker_title=<marker_title>] %}
    """
    zoom = kwargs.get('zoom', 15)
    map_type = kwargs.get('map_type', 'ROADMAP')
    marker_title = kwargs.get('marker_title')

    data = {
        'html_id': html_id,
        'lat': lat,
        'lng': lng,
        'zoom': zoom,
        'map_type': map_type
    }

    if marker_title:
        data['marker_title'] = marker_title

    return data
