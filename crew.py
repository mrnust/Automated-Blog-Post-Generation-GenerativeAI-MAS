import streamlit as st
from crewai import Crew, Process

# Import agents and tasks
from agents import news_researcher, news_writer
from tasks import research_task, write_task

# Create Crew instance
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

# User Input
title = st.text_input("Enter a Title for Your Blog Post:")

if st.button("Generate Blog Post"):
    # Update tasks with user-provided title
    crew.tasks[0].description = crew.tasks[0].description.format(topic=title)
    crew.tasks[1].description = crew.tasks[1].description.format(topic=title)

    # Execute the Crew workflow
    result = crew.kickoff(inputs={'topic': title})

    st.write(result)

