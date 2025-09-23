default hopHeight = 30

transform cleft:
    xalign 0.05 yanchor 1.0 ypos (1080 + hopHeight)

transform cright:
    xalign 0.95 yanchor 1.0 ypos (1080 + hopHeight)

transform middle:
    xalign 0.5 yanchor 1.0 ypos (1080 + hopHeight)

transform agathabreakroom:
    xalign 0.2 yanchor 1.0 ypos (1080 + hopHeight)
    zoom 0.9

transform ceebreakroom:
    xalign 0.98 yanchor 1.0 ypos (1080 + hopHeight)
    zoom 0.8

transform zoomToNormalSize:
    linear 0.5 zoom 1.0

transform shake:
    linear 0.090 xoffset -10
    linear 0.090 xoffset +0
    linear 0.090 yoffset -10
    linear 0.090 yoffset +0
    repeat

transform shake2:
    linear 0.090 xoffset -2
    linear 0.090 xoffset +0
    linear 0.090 yoffset -2
    linear 0.090 yoffset 0
    repeat

transform hop:
    linear 0.2 yoffset -hopHeight
    linear 0.3 yoffset 0
    #at hop

# transform ahop:
#     linear 0.2 yoffset -20
#     linear 0.3 yoffset 0
    #at hop

transform zoom_in:
    ease 0.25 zoom 1.25

transform zoom_normal:
    ease 0.25 zoom 1.0