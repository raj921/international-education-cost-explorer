from preswald import connect, get_df, query, plotly, text, table
import plotly.express as px

connect()
df = get_df("International_Education_Costs.csv")

sql = 'SELECT * FROM "International_Education_Costs.csv" WHERE Tuition > 10000'
filtered_df = query(sql, "International_Education_Costs.csv")

fig = px.scatter(
    df,
    x="Tuition",
    y="LivingCost",
    text="Country",
    title="Tuition vs Living Cost by Country",
    labels={"Tuition": "Tuition Cost", "LivingCost": "Living Cost"}
)
fig.update_traces(textposition="top center", marker=dict(size=12))
fig.update_layout(template="plotly_white")
plotly(fig)

text("# International Education Cost Explorer")
text("Explore tuition and living expenses across countries.")
table(filtered_df, title="Countries with Tuition > 10,000")
