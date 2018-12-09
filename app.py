import dash

app = dash.Dash()
server = app.server
app.css.append_css({"external_url": "https://cdn.jsdelivr.net/gh/lwileczek/Dash@master/undo_redo5.css"}),
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
# Need to paste github link into rawgit
# app.css.append_css({"external_url": "https://cdn.jsdelivr.net/gh/Bryce21/dash_css@master/dash_app.css"})
app.config.suppress_callback_exceptions = True
