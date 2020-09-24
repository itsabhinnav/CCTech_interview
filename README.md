input coordinates
input point
if coordinates == collinear:
    return false
else:
    polygons = form_polygon(coordinates)
for polygon in polygons:
    if polygon == simple:
        if point in polygon:
            return true
        else:
            continue
    else:
        if point in polygon:
            return true
        else:
            return false

