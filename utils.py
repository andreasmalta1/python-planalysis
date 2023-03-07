from PIL import Image


def team_colours(col):
    primary_colour = {
        "Arsenal": "#EF0107",
        "Aston Villa": "#95BFE5",
        "Bournemouth": "#DA291C",
        "Brentford": "#E30613",
        "Brighton": "#0057B8",
        "Chelsea": "#034694",
        "Crystal Palace": "#1B458F",
        "Everton": "#003399",
        "Fulham": "#241F20",
        "Leeds United": "#FFCD00",
        "Leicester City": "#003090",
        "Liverpool": "#C8102E",
        "Manchester City": "#6CABDD",
        "Manchester Utd": "#DA291C",
        "Newcastle Utd": "#241F20",
        "Nott'ham Forest": "#E53233",
        "Southampton": "#D71920",
        "Tottenham": "#132257",
        "West Ham": "#7A263A",
        "Wolves": "#FDB913",
    }

    clr = []

    for team in col:
        if team in primary_colour:
            clr.append(primary_colour[team])
        else:
            print(team)
    return clr


def secondary_team_colours(col):
    secondary_colour = {
        "Arsenal": "#9C824A",
        "Aston Villa": "#670e36",
        "Bournemouth": "#241F20",
        "Brentford": "#241F20",
        "Brighton": "#FFCD00",
        "Chelsea": "#6A7AB5",
        "Crystal Palace": "#C4122E",
        "Everton": "#FFFFFF",
        "Fulham": "#FFFFFF",
        "Leeds United": "#1D428A",
        "Leicester City": "#FDBE11",
        "Liverpool": "#00B2A9",
        "Manchester City": "#1C2C5B",
        "Manchester Utd": "#FBE122",
        "Newcastle Utd": "#41B6E6",
        "Nott'ham Forest": "#FFFFFF",
        "Southampton": "#FFC20E",
        "Tottenham": "#FFFFFF",
        "West Ham": "#1BB1E7",
        "Wolves": "#231F20",
    }
    clr = []

    for team in col:
        if team in secondary_colour:
            clr.append(secondary_colour[team])
        else:
            print(team)
    return clr


def ax_logo(ax):
    club_icon = Image.open("images/pl.png")
    ax.imshow(club_icon)
    ax.axis("off")
    return ax
