def triangle_area(side_1, side_2, side_3):
    adjecent_side = ((side_1)**2 - (side_3)**2 - (side_2)**2) / (-2*side_2)
    height = ((side_3)**2 - (adjecent_side)**2)**0.5
    area = 0.5 * side_2 * height
    return area
