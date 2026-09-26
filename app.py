import streamlit as st
import base64

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="INTELLIGENT AI STICK FOR VISUALLY IMPAIRED PERSON",
    page_icon="👨‍🦯",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==========================================================
# HELPER FUNCTIONS
# (defined once, near the top, and reused everywhere below —
#  previously image_to_base64 was duplicated inside the guides
#  section; now it lives here only)
# ==========================================================

def html(content):
    st.html(content)


def image_to_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# ==========================================================
# CUSTOM CSS
# ==========================================================

html("""
<style>

* {
    box-sizing: border-box;
}

.block-container {
    padding-top: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    max-width: 100% !important;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* ==========================================================
   TOP HEADER
========================================================== */

.top-header {
    background-color: #d80000;
    color: white;
    padding: 18px 4%;
    min-height: 145px;
    position: relative;
}

.university-name {
    font-family: "Lato", Arial, sans-serif;
    font-size: 42px;
    margin-bottom: 3px;
    line-height: 1.2;
}

.team-name {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 5px;
}

.project-name {
    font-size: 23px;
    font-weight: bold;
    line-height: 1.3;
}

.header-links {
    position: absolute;
    right: 4%;
    top: 12px;
    font-weight: bold;
    font-size: 16px;
}

.header-links span {
    margin-left: 25px;
}


/* ==========================================================
   NAVIGATION
========================================================== */

.navigation {
    background-color: #e9e9e9;
    border-bottom: 1px solid #bdbdbd;
    border-top: 1px solid #bdbdbd;
    padding: 14px 4%;
    white-space: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}

.navigation a {
    color: #333333;
    text-decoration: none;
    font-size: 18px;
    margin-right: 35px;
}

.navigation a:hover {
    color: #cc0000;
}

.home-icon {
    font-size: 24px !important;
    margin-right: 35px !important;
}


/* ==========================================================
   MAIN CONTENT
========================================================== */

.main-content {
    padding: 35px 3.2%;
    color: #222222;
}

.main-title {
    font-size: 45px;
    font-weight: 400;
    margin-bottom: 25px;
    line-height: 1.25;
}

.section-title {
    font-size: 35px;
    font-weight: 400;
    margin-top: 30px;
    margin-bottom: 20px;
}

.sub-title {
    font-size: 27px;
    font-weight: 400;
    margin-top: 25px;
    margin-bottom: 12px;
}

.paragraph {
    font-size: 18px;
    line-height: 1.65;
    margin-bottom: 20px;
    word-wrap: break-word;
}


/* ==========================================================
   TEAM
========================================================== */

.team-card {
    text-align: center;
    padding: 15px 10px;
    min-height: 180px;
}

.team-name-card {
    font-size: 20px;
    margin-bottom: 7px;
}

.team-role {
    color: #777777;
    font-size: 15px;
    margin-bottom: 10px;
}

.team-photo {
    width: 100%;
    max-width: 190px;
    aspect-ratio: 190 / 255;
    height: auto;
    object-fit: cover;
    display: block;
    margin: 0 auto 20px auto;
    border-radius: 5px;
}

.member-photo {
    width: 100%;
    max-width: 180px;
    aspect-ratio: 180 / 220;
    height: auto;
    object-fit: cover;
    display: block;
    margin: 0 auto 20px auto;
    border-radius: 5px;
}


/* ==========================================================
   DOCUMENTS
========================================================== */

.document-section {
    padding: 0 3.2% 20px 3.2%;
}

.document-link {
    color: #d60000;
    font-size: 19px;
    text-decoration: none;
    display: block;
    margin: 8px 0;
}

.document-link:hover {
    text-decoration: underline;
}


/* ==========================================================
   INFORMATION BOX
========================================================== */

.info-box {
    background-color: #f5f5f5;
    border-left: 4px solid #d60000;
    padding: 18px 22px;
    margin: 20px 0;
    font-size: 17px;
    line-height: 1.6;
    word-wrap: break-word;
}


/* ==========================================================
   FOOTER
========================================================== */

.footer {
    margin-top: 50px;
    padding: 30px;
    background-color: #eeeeee;
    text-align: center;
    color: #666666;
    font-size: 15px;
}


/* ==========================================================
   RESPONSIVE / MOBILE
   Everything above is the desktop layout. These overrides
   kick in on tablets and phones so nothing overflows,
   overlaps or gets cut off.
========================================================== */

@media (max-width: 900px) {

    .top-header {
        min-height: auto;
        padding: 16px 5%;
    }

    .university-name {
        font-size: 26px;
    }

    .team-name {
        font-size: 16px;
    }

    .project-name {
        font-size: 16px;
    }

    /* The absolute-positioned header links used to overlap
       the title text on narrow screens. On mobile they now
       drop below the header text instead, and stack. */
    .header-links {
        position: static;
        display: block;
        margin-top: 12px;
        text-align: left;
        font-size: 13px;
    }

    .header-links span {
        margin-left: 0;
        margin-right: 16px;
        display: inline-block;
    }

    .navigation {
        padding: 10px 4%;
    }

    .navigation a {
        font-size: 15px;
        margin-right: 20px;
    }

    .main-content {
        padding: 24px 5%;
    }

    .main-title {
        font-size: 26px;
    }

    .section-title {
        font-size: 22px;
    }

    .sub-title {
        font-size: 19px;
    }

    .paragraph {
        font-size: 16px;
    }

    .team-name-card {
        font-size: 17px;
    }

    .team-role {
        font-size: 14px;
    }

    .document-link {
        font-size: 17px;
    }

    .info-box {
        font-size: 15px;
        padding: 14px 16px;
    }
}

@media (max-width: 480px) {

    .university-name {
        font-size: 21px;
    }

    .main-title {
        font-size: 22px;
    }

    .section-title {
        font-size: 20px;
    }
}

</style>
""")


# ==========================================================
# HEADER
# ==========================================================

html("""
<div class="top-header">

    <div class="university-name">
        SIDDAGANGA INSTITUTE OF TECHNOLOGY
    </div>

    <div class="team-name">
        -----Team 2026-27
    </div>

    <div class="project-name">
        INTELLIGENT AI STICK FOR VISUALLY IMPAIRED PERSON
    </div>

    <div class="header-links">
        <span>ECE @ SIT</span>
        <span>WORK IS WORKSHIP</span>
    </div>

</div>
""")


# ==========================================================
# NAVIGATION
# ==========================================================

html("""
<div class="navigation">

    <a href="#home" class="home-icon">⌂</a>

    <a href="#team">TEAM</a>

    <a href="#reports">WEEKLY REPORTS</a>

    <a href="#documents">DESIGN DOCUMENTS</a>

    <a href="#github">GIT ORGANIZATION</a>

    <a href="#poster">PROJECT POSTER</a>

    <a href="#presentation">PRESENTATION</a>

</div>
""")


# ==========================================================
# HOME / PROJECT OVERVIEW
# ==========================================================

html("""
<div id="home" class="main-content">

    <div class="main-title">
        An Edge Vision Assistive Guidance Cane
        for the Visually Impaired
    </div>

    <div class="section-title">
        Project Overview
    </div>

    <div class="sub-title">
        Abstract
    </div>

    <div class="paragraph">

        Visually impaired individuals often face difficulties
        while moving independently in unfamiliar indoor and
        outdoor environments. A conventional white cane is an important mobility aid
        that helps users detect obstacles through physical
        contact. However, it provides limited information about
        the type, location and distance of objects in the
        surrounding environment. To address these limitations, this project proposes an
        Edge Vision Assistive Guidance Cane for the Visually
        Impaired. The proposed system integrates a camera, distance
        sensor, Raspberry Pi 5, computer vision, object
        detection and audio/vibration feedback into a portable
        walking cane. The Raspberry Pi 5 performs image processing and object
        detection locally. The system can identify common
        objects and obstacles such as people, vehicles, chairs,
        walls and poles.

    </div>

</div>
""")


html("""
<div class="main-content">

    <div class="section-title">
        Objectives
    </div>

    <div class="paragraph">

        <b>1. Edge-Based Perception</b>

        <br><br>

        To develop an edge-based perception system using a
        camera interfaced with a Raspberry Pi 5 that is capable
        of detecting and recognizing objects and obstacles in
        the user's surroundings in real time and estimating
        their proximity.

    </div>


    <div class="paragraph">

        <b>2. Autonomous Guidance</b>

        <br><br>

        To enable autonomous guidance in which the system
        provides spoken turn-by-turn directions when the user
        wishes to travel to a chosen destination and provides
        avoidance instructions such as "Move Left / Right"
        to help the user steer clear of obstacles.

    </div>


    <div class="paragraph">

        <b>3. Portable Assistive System</b>

        <br><br>

        To integrate environmental perception and guidance into
        a single portable cane prototype so that obstacle
        awareness and destination navigation work together
        through audio and vibration feedback while retaining
        the basic functionality of a conventional white cane.

    </div>

</div>
""")


# ==========================================================
# PROJECT GUIDES  (TEAM anchor target)
# ==========================================================

html("""
<div id="team" class="main-content">

    <div class="section-title">
        Project Guides
    </div>

    <div style="margin-bottom: 20px;">
        <a href="#members"
           style="
               color: #d60000;
               text-decoration: none;
               font-size: 16px;
           ">
            ↓ View Team Members
        </a>
    </div>

</div>
""")

guides = [
    (
        "Dr. K V Suresh",
        "Professor",
        "Department of ECE, SIT",
        "assets/team/Dr.-K-V-Suresh.jpg"
    ),
    (
        "Sandesh G V",
        "Founder / Software Developer",
        "Nasken Health, Boston, United States",
        "assets/team/sandesh_g_v.jpg"
    )
]

cols = st.columns(2)

for col, (name, designation, organization, photo) in zip(cols, guides):

    with col:

        image_base64 = image_to_base64(photo)

        html(f"""
        <div style="text-align: center; padding: 10px 20px 30px 20px;">

            <img
                src="data:image/jpeg;base64,{image_base64}"
                class="team-photo"
            >

            <div class="team-name-card">
                {name}
            </div>

            <div class="team-role">
                {designation}
            </div>

            <div class="team-role">
                {organization}
            </div>

        </div>
        """)


# ==========================================================
# TEAM MEMBERS
# ==========================================================

html("""
<div id="members" class="main-content">

    <div class="section-title">
        Team Members
    </div>

    <div style="margin-bottom: 20px;">
        <a href="#team"
           style="
               color: #d60000;
               text-decoration: none;
               font-size: 16px;
           ">
            ↑ Back to Project Guides
        </a>
    </div>

</div>
""")

team_members = [
    (
        "Abhishek Kumar Singh",
        "1SI24EC002",
        "Project Member",
        "assets/team/photo_gtnew.jpg"
    ),
    (
        "Avinash",
        "1SI24EC017",
        "Project Member",
        "assets/team/avinash.jpeg"
    ),
    (
        "Kartik Kumar Singh",
        "1SI24EC053",
        "Project Member",
        "assets/team/kartik.jpeg"
    ),
    (
        "Lakshisha V M",
        "1SI24EC056",
        "Project Member",
        "assets/team/photomini.jpg"
    )
]

cols = st.columns(4)

for col, (name, usn, role, photo) in zip(cols, team_members):

    with col:

        image_base64 = image_to_base64(photo)

        html(f"""
        <div style="text-align: center; padding: 10px 10px 30px 10px;">

            <img
                src="data:image/jpeg;base64,{image_base64}"
                class="member-photo"
            >

            <div class="team-name-card">
                {name}
            </div>

            <div class="team-role">
                {usn}
            </div>

            <div class="team-role">
                {role}
            </div>

            <div class="team-role">
                Electronics & Communication Engineering
            </div>

        </div>
        """)


# ==========================================================
# WEEKLY REPORTS
# ==========================================================

html("""
<div id="reports" class="document-section">

    <div class="section-title">
        Weekly Reports
    </div>

    <div class="paragraph">
        <b>2026 Academic Year:</b>
    </div>

    <a class="document-link" href="#">
        Report 1 — Project Introduction
    </a>

    <a class="document-link" href="#">
        Report 2 — Literature Survey
    </a>

    <a class="document-link" href="#">
        Report 3 — System Requirements
    </a>

    <a class="document-link" href="#">
        Report 4 — Hardware Selection
    </a>

    <a class="document-link" href="#">
        Report 5 — Software Development
    </a>

    <a class="document-link" href="#">
        Report 6 — Prototype Development
    </a>

    <a class="document-link" href="#">
        Report 7 — Testing and Validation
    </a>

</div>
""")


# ==========================================================
# DESIGN DOCUMENTS
# ==========================================================

html("""
<div id="documents" class="document-section">

    <div class="section-title">
        Design Documents
    </div>

    <div class="paragraph">
        <b>Project Documentation</b>
    </div>

    <a class="document-link" href="#">
        Initial Design Document
    </a>

    <a class="document-link" href="#">
        System Requirements Document
    </a>

    <a class="document-link" href="#">
        Hardware Design Document
    </a>

    <a class="document-link" href="#">
        Software Design Document
    </a>

    <a class="document-link" href="#">
        Final Design Document
    </a>

</div>
""")


# ==========================================================
# GITHUB
# ==========================================================

html("""
<div id="github" class="document-section">

    <div class="section-title">
        Git Organization
    </div>

    <div class="paragraph">

        The source code and development files for the
        First Responder Drone project are maintained using
        Git and GitHub.

    </div>

    <a
        class="document-link"
        href="https://github.com/"
        target="_blank"
    >
        GitHub Organization
    </a>

    <a
        class="document-link"
        href="https://github.com/"
        target="_blank"
    >
        Project Repository
    </a>

</div>
""")


# ==========================================================
# PROJECT POSTER
# ==========================================================

html("""
<div id="poster" class="document-section">

    <div class="section-title">
        Final Project Poster
    </div>

    <div class="paragraph">

        The final project poster provides a summary of the
        problem statement, proposed solution, system design,
        implementation and project results.

    </div>

    <a class="document-link" href="#">
        View Project Poster
    </a>

</div>
""")


# ==========================================================
# PRESENTATION
# ==========================================================

html("""
<div id="presentation" class="document-section">

    <div class="section-title">
        Industry Review Panel Presentation
    </div>

    <div class="paragraph">

        The industry review presentation provides an overview
        of the project development, system architecture,
        implementation and testing.

    </div>

    <a class="document-link" href="#">
        Industry Review Presentation
    </a>

    <div class="section-title">
        Faculty Presentation
    </div>

    <a class="document-link" href="#">
        Faculty Project Presentation
    </a>

</div>
""")


# ==========================================================
# PROJECT INFORMATION
# ==========================================================

html("""
<div class="document-section">

    <div class="section-title">
        Project Information
    </div>

    <div class="info-box">

        <b>Institution:</b>
        Siddaganga Institute of Technology
        <br>

        <b>Department:</b>
        Electronics and Communication Engineering
        <br>

        <b>Project:</b>
        Intelligent AI Stick for Visually Impaired Person
        <br>

        <b>Project Type:</b>
        Academic Project
        <br>

        <b>Academic Year:</b>
        2026
        <br>

        <b>Domain:</b>
        AI/ML/DL, Embedded Systems, IoT

    </div>

</div>
""")


# ==========================================================
# FOOTER
# ==========================================================

html("""
<div class="footer">

    Mini project
    <br>

    Department of Electronics and Communication Engineering
    <br>

    Siddaganga Institute of Technology
    <br>

    Academic Year 2026-27

</div>
""")
