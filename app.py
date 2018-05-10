import dash

app = dash.Dash()
server = app.server
app.css.append_css({"external_url": "https://rawgit.com/lwileczek/Dash/master/undo_redo5.css"})
app.config.suppress_callback_exceptions = True
