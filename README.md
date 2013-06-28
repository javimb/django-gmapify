# django-gmapify

Add a Google Map to a template with a simple tag.

Django-gmapify provides an easy way to manage the Google Maps JavaScript API v3 using a simple tag:

    {% gmapify "map-canvas" 36.84531718210699 -2.4523544311523438 %}

## Installation

Using `pip`:

    $ pip install django-gmapify

Or cloning the project from github:

    $ git clone git@javimb/django-gmapify.git
$ cd django-gmapify
    $ pip install -r requirements.txt

## Usage

Add `gmapify` to `INSTALLED_APPS`:

    INSTALLED_APPS = (
    ...
    'gmapify',
    ...)

Create a div in the template. The map will fill this div, so it has to have width and heigth:

    <div id="map-canvas" style="width:500px;height:500px;"></div>

Load and use the provided `gmapify` tag in the template:

    {% load gmapify %}
    {% gmapify <html_id> <lat> <lng> [zoom=<zoom>] [map_type=<map_type>] [marker_title=<marker_title>] %}

Django-gmapify provides all the JavaScript stuff for Google Maps API v3, so put the `gmapify` tag at the end of the template.

### Optional args

 - **zoom:** The initial resolution at which to display the map, where zoom 0 corresponds to a map of the Earth fully zoomed out, and higher zoom levels zoom in at a higher resolution. 15 by default.
 - **map_type:** The initial map type. ROADMAP by default. The following map types are supported:
    - **ROADMAP:** displays the normal, default 2D tiles of Google Maps.
    - **SATELLITE:** displays photographic tiles.
    - **HYBRID:** displays a mix of photographic tiles and a tile layer for prominent features (roads, city names).
    - **TERRAIN:** displays physical relief tiles for displaying elevation and water features (mountains, rivers, etc.).
 - **marker_title:** The title of the marker. If it's not provided, no marker will be displayed.

##Example

    {% load gmapify%}

    {% block styles %}
        {{ block.super }}
        <style type="text/css">
            #map {
                width: 100%;
                height: 500px;
            }
        </style>
    {% endblock style%}

    {% block content %}
        <div id="map"></div>
    {% endblock content%}

    {% block js %}
        {% gmapify "map" 36.84531718210699 -2.4523544311523438 zoom=18 marker_title="Almeria" %}
    {% endblock js %}