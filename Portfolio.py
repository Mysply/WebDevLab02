import streamlit as st
import info  # Import data from info.py

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Bluey's Portfolio", page_icon="🐶", layout="wide")

# --- HEADER SECTION ---
st.title("🐶 Bluey's Portfolio")
st.image(info.profile_picture, width=200)
st.write(info.about_me)

# --- CONTACT INFO ---
st.header("📬 Connect with Me")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(info.linkedin_image_url, width=50)
    st.markdown(f"[LinkedIn]({info.my_linkedin_url})")

with col2:
    st.image(info.github_image_url, width=50)
    st.markdown(f"[GitHub]({info.my_github_url})")

with col3:
    st.image(info.email_image_url, width=50)
    st.markdown(f"[Email](mailto:{info.my_email_address})")

# --- EDUCATION ---
st.header("🎓 Education")
st.write(
    f"**{info.education_data['Degree']}**\n"
    f"{info.education_data['Institution']} - {info.education_data['Location']}\n"
    f"Graduation: {info.education_data['Graduation Date']} | GPA: {info.education_data['GPA']}"
)

# --- COURSES ---
st.header("📚 Relevant Courses")
for i in range(len(info.course_data["code"])):
    st.write(
        f"**{info.course_data['code'][i]}** - {info.course_data['names'][i]}"
        f" (Taken: {info.course_data['semester_taken'][i]})"
    )
    st.caption(info.course_data['skills'][i])

# --- EXPERIENCE ---
st.header("💼 Experience")
for role, (desc, img) in info.experience_data.items():
    st.subheader(role)
    st.image(img, width=200)
    for bullet in desc:
        st.write(f"- {bullet}")

# --- PROJECTS ---
st.header("🚀 Projects")
for proj, desc in info.projects_data.items():
    st.subheader(proj)
    st.write(desc)

# --- PROGRAMMING SKILLS ---
st.header("💻 Programming Skills")
for skill, level in info.programming_data.items():
    st.write(f"{info.programming_icons[skill]} **{skill}**: {level}% Proficiency")
    st.progress(level / 100)

# --- SPOKEN LANGUAGES ---
st.header("🗣️ Spoken Languages")
for lang, fluency in info.spoken_data.items():
    st.write(f"{info.spoken_icons[lang]} **{lang}** - {fluency}")

# --- LEADERSHIP ---
st.header("🌟 Leadership & Activities")
for role, (desc, img) in info.leadership_data.items():
    st.subheader(role)
    st.image(img, width=200)
    for bullet in desc:
        st.write(f"- {bullet}")

# --- NAVIGATION TO MULTI-PAGE APP ---
st.sidebar.title("🔗 Navigate")
st.sidebar.page_link("Home_Page.py", label="🏠 Home")
st.sidebar.page_link("PhaseII.py", label="📊 Data Exploration")
