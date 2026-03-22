import streamlit as st

# ─── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Gayathri Gollapolu | Portfolio",
    page_icon="🌿",
    layout="wide",
)

# ─── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
  --teal: #2a9d8f;
  --teal-dark: #1f7a6e;
  --teal-light: #e0f4f1;
  --green: #57cc99;
  --text: #1a2420;
  --muted: #5a7068;
  --border: #d4e8e3;
  --bg: #f5f7f5;
  --surface: #ffffff;
}

html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif !important;
  background-color: var(--bg);
  color: var(--text);
}

/* hide streamlit default header/footer */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── HERO ── */
.hero {
  background: linear-gradient(135deg, #f0faf8 0%, #e8f7f4 50%, #f5f7f5 100%);
  padding: 5rem 8vw 4rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 3rem;
  flex-wrap: wrap;
  border-bottom: 1px solid var(--border);
}
.hero-left { flex: 1.2; min-width: 280px; }
.hero-tag {
  display: inline-block;
  background: var(--teal-light);
  color: var(--teal-dark);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.35rem 1rem;
  border-radius: 20px;
  margin-bottom: 1.2rem;
}
.hero-name {
  font-family: 'DM Serif Display', serif !important;
  font-size: clamp(2.5rem, 5vw, 4rem);
  line-height: 1.1;
  letter-spacing: -0.03em;
  color: var(--text);
  margin-bottom: 0.3rem;
}
.hero-name em { color: var(--teal); font-style: italic; }
.hero-sub {
  font-size: 1rem;
  color: var(--muted);
  font-weight: 300;
  max-width: 420px;
  line-height: 1.7;
  margin-bottom: 2rem;
}
.hero-btns { display: flex; gap: 1rem; flex-wrap: wrap; }
.btn-primary {
  background: var(--teal);
  color: #fff !important;
  padding: 0.7rem 1.6rem;
  border-radius: 5px;
  text-decoration: none !important;
  font-weight: 600;
  font-size: 0.88rem;
  transition: background 0.2s;
  display: inline-block;
}
.btn-primary:hover { background: var(--teal-dark) !important; }
.btn-outline {
  border: 1.5px solid var(--teal);
  color: var(--teal) !important;
  padding: 0.7rem 1.6rem;
  border-radius: 5px;
  text-decoration: none !important;
  font-weight: 600;
  font-size: 0.88rem;
  display: inline-block;
}
.hero-right { flex: 1; min-width: 260px; }
.profile-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 8px 40px rgba(42,157,143,0.08);
  max-width: 380px;
}
.avatar {
  width: 80px; height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--teal), var(--green));
  display: flex; align-items: center; justify-content: center;
  font-family: 'DM Serif Display', serif;
  font-size: 1.8rem;
  color: white;
  margin-bottom: 1rem;
}
.profile-name {
  font-family: 'DM Serif Display', serif;
  font-size: 1.25rem;
  color: var(--text);
}
.profile-role { font-size: 0.83rem; color: var(--muted); margin-bottom: 1.2rem; }
.stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.8rem;
  padding: 1.2rem 0;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  margin-bottom: 1rem;
  text-align: center;
}
.stat-num {
  font-family: 'DM Serif Display', serif;
  font-size: 1.5rem;
  color: var(--teal);
  display: block;
}
.stat-label { font-size: 0.7rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }
.contact-link {
  display: flex; align-items: center; gap: 0.5rem;
  font-size: 0.8rem; color: var(--muted);
  text-decoration: none; margin-bottom: 0.4rem;
}
.dot { width: 6px; height: 6px; border-radius: 50%; background: var(--teal); flex-shrink: 0; }

/* ── SECTIONS ── */
.section {
  padding: 4.5rem 8vw;
}
.section-alt { background: var(--surface); }
.section-label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--teal);
  margin-bottom: 0.4rem;
}
.section-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  color: var(--text);
  letter-spacing: -0.02em;
  margin-bottom: 0.5rem;
}
.section-line {
  width: 44px; height: 3px;
  background: var(--teal);
  border-radius: 2px;
  margin-bottom: 2.5rem;
}

/* ── ABOUT ── */
.about-grid { display: grid; grid-template-columns: 1.2fr 1fr; gap: 3rem; align-items: start; flex-wrap: wrap; }
.about-p { font-size: 0.97rem; color: var(--muted); margin-bottom: 0.9rem; font-weight: 300; line-height: 1.75; }
.about-p strong { color: var(--text); font-weight: 600; }
.edu-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-left: 4px solid var(--teal);
  border-radius: 10px;
  padding: 1.2rem 1.4rem;
  margin-bottom: 1rem;
}
.edu-year { font-size: 0.75rem; font-weight: 700; color: var(--teal); letter-spacing: 0.05em; }
.edu-degree { font-size: 0.95rem; font-weight: 600; color: var(--text); margin: 0.15rem 0; }
.edu-inst { font-size: 0.82rem; color: var(--muted); }
.cgpa { display: inline-block; background: var(--teal-light); color: var(--teal-dark); font-size: 0.72rem; font-weight: 700; padding: 0.18rem 0.55rem; border-radius: 20px; margin-top: 0.3rem; }

/* ── SKILLS ── */
.skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.2rem; }
.skill-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.4rem;
}
.skill-card-title {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--teal);
  padding-bottom: 0.7rem;
  border-bottom: 1px solid var(--border);
  margin-bottom: 0.9rem;
}
.skill-bar { margin-bottom: 0.8rem; }
.skill-bar-label { display: flex; justify-content: space-between; font-size: 0.82rem; font-weight: 500; color: var(--text); margin-bottom: 0.3rem; }
.skill-bar-track { height: 5px; background: var(--border); border-radius: 3px; overflow: hidden; }
.skill-bar-fill { height: 100%; border-radius: 3px; background: linear-gradient(90deg, var(--teal), var(--green)); }
.tag-cloud { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.tag {
  background: var(--bg);
  border: 1px solid var(--border);
  color: var(--text);
  font-size: 0.78rem;
  font-weight: 500;
  padding: 0.28rem 0.7rem;
  border-radius: 20px;
}

/* ── PROJECTS ── */
.projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.3rem; }
.proj-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.7rem;
  position: relative;
  overflow: hidden;
}
.proj-num {
  font-family: 'DM Serif Display', serif;
  font-size: 2.2rem;
  color: var(--teal-light);
  line-height: 1;
  margin-bottom: 0.8rem;
}
.proj-title { font-size: 0.97rem; font-weight: 700; color: var(--text); margin-bottom: 0.5rem; }
.proj-desc { font-size: 0.83rem; color: var(--muted); line-height: 1.65; margin-bottom: 1rem; }
.proj-tags { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.proj-tag { background: var(--teal-light); color: var(--teal-dark); font-size: 0.7rem; font-weight: 700; padding: 0.18rem 0.55rem; border-radius: 20px; }

/* ── EXPERIENCE ── */
.timeline { position: relative; padding-left: 2rem; }
.timeline::before { content: ''; position: absolute; left: 6px; top: 8px; bottom: 8px; width: 2px; background: linear-gradient(to bottom, var(--teal), var(--green)); border-radius: 1px; }
.timeline-item { position: relative; margin-bottom: 2rem; padding-left: 1.5rem; }
.timeline-item::before { content: ''; position: absolute; left: -1.6rem; top: 6px; width: 12px; height: 12px; border-radius: 50%; background: var(--teal); border: 2px solid var(--bg); box-shadow: 0 0 0 2px var(--teal); }
.tl-date { font-size: 0.73rem; font-weight: 700; letter-spacing: 0.08em; color: var(--teal); text-transform: uppercase; margin-bottom: 0.2rem; }
.tl-role { font-size: 0.97rem; font-weight: 600; color: var(--text); }
.tl-company { font-size: 0.85rem; color: var(--muted); margin-bottom: 0.4rem; }
.tl-desc { font-size: 0.83rem; color: var(--muted); line-height: 1.65; }

/* ── CERTIFICATIONS ── */
.cert-list { display: flex; flex-direction: column; gap: 0.8rem; }
.cert-item { display: flex; align-items: center; gap: 1rem; background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 1rem 1.2rem; }
.cert-icon-box { width: 38px; height: 38px; border-radius: 8px; background: linear-gradient(135deg, var(--teal), var(--green)); display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0; }
.cert-name { font-size: 0.85rem; font-weight: 600; color: var(--text); }
.cert-issuer { font-size: 0.75rem; color: var(--muted); }

/* ── FOOTER ── */
.footer {
  background: #1a2420;
  color: rgba(255,255,255,0.45);
  text-align: center;
  padding: 2rem 4rem;
  font-size: 0.8rem;
}
.footer a { color: var(--teal); text-decoration: none; }
.footer strong { color: white; }

/* ── TWO-COL ── */
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }
.col-title { font-family: 'DM Serif Display', serif; font-size: 1.25rem; color: var(--text); margin-bottom: 1.5rem; }

@media (max-width: 768px) {
  .hero, .about-grid, .two-col { flex-direction: column; grid-template-columns: 1fr; }
  .section { padding: 3rem 1.5rem; }
}
</style>
""", unsafe_allow_html=True)


# ─── HERO ─────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-left">
    <span class="hero-tag">🌿 Open to Internships &amp; Opportunities</span>
    <div class="hero-name">Building the <em>Future</em><br>with Data &amp; AI</div>
    <p class="hero-sub">B.Tech AI &amp; Data Science student passionate about turning data into meaningful decisions. Python · Java · Machine Learning · Data Analytics.</p>
    <div class="hero-btns">
      <a href="mailto:gayathrigollapolu@gmail.com" class="btn-primary">✉️ Get In Touch</a>
      <a href="https://www.linkedin.com/in/gayathri-gollapolu-741278362" target="_blank" class="btn-outline">LinkedIn ↗</a>
      <a href="https://github.com/gayathri200508" target="_blank" class="btn-outline">GitHub ↗</a>
    </div>
  </div>
  <div class="hero-right">
    <div class="profile-card">
      <div class="avatar">GG</div>
      <div class="profile-name">Gayathri Gollapolu</div>
      <div class="profile-role">AI &amp; Data Science · AITS Tirupati</div>
      <div class="stats-grid">
        <div><span class="stat-num">8.6</span><span class="stat-label">CGPA</span></div>
        <div><span class="stat-num">3+</span><span class="stat-label">Internships</span></div>
        <div><span class="stat-num">6+</span><span class="stat-label">Projects</span></div>
        <div><span class="stat-num">5+</span><span class="stat-label">Certifications</span></div>
      </div>
      <a href="mailto:gayathrigollapolu@gmail.com" class="contact-link"><span class="dot"></span> gayathrigollapolu@gmail.com</a>
      <a href="https://github.com/gayathri200508" class="contact-link"><span class="dot"></span> github.com/gayathri200508</a>
      <span class="contact-link"><span class="dot"></span> Nellore, Andhra Pradesh, India</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─── ABOUT ────────────────────────────────────────────────────
st.markdown("""
<div class="section" id="about">
  <p class="section-label">Who I Am</p>
  <div class="section-title">About Me</div>
  <div class="section-line"></div>
  <div class="about-grid">
    <div>
      <p class="about-p">Hi! I'm <strong>Gayathri Gollapolu</strong>, a 3rd-year B.Tech student specializing in <strong>Artificial Intelligence &amp; Data Science</strong> at Annamacharya Institute of Technology and Sciences, Tirupati.</p>
      <p class="about-p">I'm passionate about building data-driven solutions — from machine learning models and recommendation systems to interactive AI apps. My journey includes hands-on internships, real-world projects, and continuous learning.</p>
      <p class="about-p">Currently interning as an <strong>ML Engineer at Cognifyz Technologies</strong>, working on restaurant rating prediction and recommendation systems using real-world Zomato datasets.</p>
      <p class="about-p">I'm also exploring <strong>Salesforce</strong> as a parallel career track and maintain daily practice of <strong>Java &amp; Data Structures</strong> for placement preparation.</p>
    </div>
    <div>
      <div class="edu-card">
        <div class="edu-year">Aug 2023 – Aug 2027</div>
        <div class="edu-degree">B.Tech – Artificial Intelligence &amp; Data Science</div>
        <div class="edu-inst">Annamacharya Institute of Technology &amp; Sciences, Tirupati</div>
        <span class="cgpa">CGPA: 8.6</span>
      </div>
      <div class="edu-card">
        <div class="edu-year">Intermediate · 2021 – 2023</div>
        <div class="edu-degree">MPC Stream</div>
        <div class="edu-inst">Viswateja Junior College, Duttalur</div>
      </div>
      <div class="edu-card">
        <div class="edu-year">SSC · 2022 – 2023</div>
        <div class="edu-degree">Secondary Education (10th)</div>
        <div class="edu-inst">ZPP High School, Vinjamur Mandal</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─── SKILLS ───────────────────────────────────────────────────
st.markdown("""
<div class="section section-alt" id="skills">
  <p class="section-label">What I Know</p>
  <div class="section-title">Skills</div>
  <div class="section-line"></div>
  <div class="skills-grid">

    <div class="skill-card">
      <div class="skill-card-title">Programming Languages</div>
      <div class="skill-bar">
        <div class="skill-bar-label"><span>Python</span><span>85%</span></div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:85%"></div></div>
      </div>
      <div class="skill-bar">
        <div class="skill-bar-label"><span>Java</span><span>78%</span></div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:78%"></div></div>
      </div>
      <div class="skill-bar">
        <div class="skill-bar-label"><span>SQL</span><span>75%</span></div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:75%"></div></div>
      </div>
    </div>

    <div class="skill-card">
      <div class="skill-card-title">Data Science &amp; ML</div>
      <div class="tag-cloud">
        <span class="tag">Machine Learning</span><span class="tag">Pandas</span>
        <span class="tag">NumPy</span><span class="tag">Scikit-learn</span>
        <span class="tag">Data Wrangling</span><span class="tag">EDA</span>
        <span class="tag">Feature Engineering</span><span class="tag">Statistics</span>
      </div>
    </div>

    <div class="skill-card">
      <div class="skill-card-title">Tools &amp; Platforms</div>
      <div class="tag-cloud">
        <span class="tag">Power BI</span><span class="tag">Jupyter Notebook</span>
        <span class="tag">VS Code</span><span class="tag">MongoDB</span>
        <span class="tag">Git &amp; GitHub</span><span class="tag">Streamlit</span>
        <span class="tag">Flask</span><span class="tag">SQLite</span>
      </div>
    </div>

    <div class="skill-card">
      <div class="skill-card-title">Other Skills</div>
      <div class="tag-cloud">
        <span class="tag">Salesforce Trailhead</span>
        <span class="tag">Groq API</span><span class="tag">LLaMA 3</span>
        <span class="tag">Dynamic Programming</span>
        <span class="tag">Data Visualization</span>
        <span class="tag">Problem Solving</span>
      </div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)


# ─── PROJECTS ─────────────────────────────────────────────────
st.markdown("""
<div class="section" id="projects">
  <p class="section-label">What I Built</p>
  <div class="section-title">Projects</div>
  <div class="section-line"></div>
  <div class="projects-grid">

    <div class="proj-card">
      <div class="proj-num">01</div>
      <div class="proj-title">AI Study Note Generator</div>
      <p class="proj-desc">Streamlit-powered AI app generating study notes using Groq API with LLaMA 3. Presented at a college hackathon and deployed to GitHub.</p>
      <div class="proj-tags">
        <span class="proj-tag">Python</span><span class="proj-tag">Streamlit</span>
        <span class="proj-tag">Groq API</span><span class="proj-tag">LLaMA 3</span>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-num">02</div>
      <div class="proj-title">Restaurant Rating Prediction</div>
      <p class="proj-desc">ML model to predict restaurant ratings from Zomato dataset. Feature engineering, handled imbalanced data, built regression models. (Cognifyz Internship Task 1)</p>
      <div class="proj-tags">
        <span class="proj-tag">Python</span><span class="proj-tag">Scikit-learn</span>
        <span class="proj-tag">Pandas</span><span class="proj-tag">ML</span>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-num">03</div>
      <div class="proj-title">Restaurant Recommendation System</div>
      <p class="proj-desc">Content-based recommendation system on Zomato dataset, filtering restaurants by cuisine, location, and rating preferences. (Cognifyz Internship Task 2)</p>
      <div class="proj-tags">
        <span class="proj-tag">Python</span><span class="proj-tag">Pandas</span>
        <span class="proj-tag">Cosine Similarity</span>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-num">04</div>
      <div class="proj-title">AI Crop Disease Detection App</div>
      <p class="proj-desc">AI-based crop disease detection concept for rural Andhra Pradesh farmers. Built and pitched as Team BRIGHT at India Innovates 2026.</p>
      <div class="proj-tags">
        <span class="proj-tag">AI/ML</span><span class="proj-tag">Image Classification</span>
        <span class="proj-tag">Python</span>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-num">05</div>
      <div class="proj-title">Data Analytics Dashboard</div>
      <p class="proj-desc">End-to-end EDA on synthetic Indian shopping dataset — data wrangling, SQL via SQLite, multivariate analysis, and PowerPoint dashboard. (ApexPlanet Internship)</p>
      <div class="proj-tags">
        <span class="proj-tag">Python</span><span class="proj-tag">SQL</span>
        <span class="proj-tag">Power BI</span><span class="proj-tag">Pandas</span>
      </div>
    </div>

    <div class="proj-card">
      <div class="proj-num">06</div>
      <div class="proj-title">Flask Portfolio Builder</div>
      <p class="proj-desc">Dynamic resume/portfolio builder built with Python Flask — users input details and generate a personalized portfolio webpage instantly.</p>
      <div class="proj-tags">
        <span class="proj-tag">Python</span><span class="proj-tag">Flask</span>
        <span class="proj-tag">HTML/CSS</span>
      </div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)


# ─── EXPERIENCE + CERTIFICATIONS ─────────────────────────────
st.markdown("""
<div class="section section-alt" id="experience">
  <p class="section-label">My Journey</p>
  <div class="section-title">Experience &amp; Certifications</div>
  <div class="section-line"></div>
  <div class="two-col">

    <div>
      <div class="col-title">Work Experience</div>
      <div class="timeline">

        <div class="timeline-item">
          <div class="tl-date">Jan 2026 – Apr 2026</div>
          <div class="tl-role">Machine Learning Intern</div>
          <div class="tl-company">Cognifyz Technologies · Remote</div>
          <p class="tl-desc">Working on ML tasks using real-world Zomato dataset — restaurant rating prediction (regression models) and content-based recommendation system.</p>
        </div>

        <div class="timeline-item">
          <div class="tl-date">2025 · 60 Days</div>
          <div class="tl-role">Data Analytics Intern</div>
          <div class="tl-company">ApexPlanet Software Pvt. Ltd · Remote</div>
          <p class="tl-desc">Data wrangling on Indian shopping dataset, full EDA with SQL, multivariate analysis, and visual dashboard presentation.</p>
        </div>

        <div class="timeline-item">
          <div class="tl-date">2024 · Virtual</div>
          <div class="tl-role">Data Analytics Virtual Intern</div>
          <div class="tl-company">Deloitte Australia · via Forage</div>
          <p class="tl-desc">Simulated real-world data analytics tasks — data interpretation, dashboard creation, and business insight generation.</p>
        </div>

        <div class="timeline-item">
          <div class="tl-date">2025 · Ongoing</div>
          <div class="tl-role">E&amp;ICT Academy Certification</div>
          <div class="tl-company">IIT Roorkee · Data Science &amp; AI</div>
          <p class="tl-desc">Pursuing certification in Data Science and AI from IIT Roorkee — covering ML, deep learning, and AI concepts.</p>
        </div>

      </div>
    </div>

    <div>
      <div class="col-title">Certifications</div>
      <div class="cert-list">
        <div class="cert-item">
          <div class="cert-icon-box">📊</div>
          <div><div class="cert-name">Data Visualisation Job Simulation</div><div class="cert-issuer">Tata Group · Forage</div></div>
        </div>
        <div class="cert-item">
          <div class="cert-icon-box">🍃</div>
          <div><div class="cert-name">MongoDB Overview</div><div class="cert-issuer">MongoDB University</div></div>
        </div>
        <div class="cert-item">
          <div class="cert-icon-box">📈</div>
          <div><div class="cert-name">Power BI Micro Course</div><div class="cert-issuer">Microsoft / Udemy</div></div>
        </div>
        <div class="cert-item">
          <div class="cert-icon-box">🔍</div>
          <div><div class="cert-name">Data Analytics Job Simulation</div><div class="cert-issuer">Deloitte Australia · Forage</div></div>
        </div>
        <div class="cert-item">
          <div class="cert-icon-box">🤖</div>
          <div><div class="cert-name">AI Tools Workshop</div><div class="cert-issuer">Industry Workshop</div></div>
        </div>
        <div class="cert-item">
          <div class="cert-icon-box">☁️</div>
          <div><div class="cert-name">Salesforce Trailhead Modules</div><div class="cert-issuer">Agentforce, Platform Basics &amp; more</div></div>
        </div>
      </div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)


# ─── FOOTER ───────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <p>Designed &amp; built by <strong>Gayathri Gollapolu</strong> ·
    <a href="mailto:gayathrigollapolu@gmail.com">gayathrigollapolu@gmail.com</a> ·
    <a href="https://www.linkedin.com/in/gayathri-gollapolu-741278362" target="_blank">LinkedIn</a> ·
    <a href="https://github.com/gayathri200508" target="_blank">GitHub</a>
  </p>
  <p style="margin-top:0.4rem;font-size:0.72rem;">© 2025 Gayathri Gollapolu · Tirupati, Andhra Pradesh</p>
</div>
""", unsafe_allow_html=True)
