from flask import Flask, render_template, Markup, render_template_string, url_for
from flask_flatpages import FlatPages, pygmented_markdown

# create the application
app = Flask(__name__)
pages = FlatPages(app)

# define a custom renderer to enable url_for in flatpages
def prerender_jinja(text):
  prerendered_body = render_template_string(Markup(text))
  return pygmented_markdown(prerendered_body)

APP_PREFIX='/'
app.config.update(dict(
  FREEZER_DESTINATION = 'build',
  FREEZER_DESTINATION_IGNORE = ['.GIT*', 'CNAME', '.gitignore', 'readme.md'],
  FREEZER_BASE_URL = 'http://engelhard.georgetown.edu' + APP_PREFIX,
  FREEZER_RELATIVE_URLS = False,
  FLATPAGES_HTML_RENDERER = prerender_jinja,
))

profiles = []
for p in pages:
  if ('profiles' in p.path) and p.body:
    profiles.append(p)
profiles = sorted(profiles, key=lambda k: (k.meta['faculty']))

# routes

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/profiles/')
def profile_list():
  return render_template('profile_list.html', profiles=profiles)

@app.route('/<path:path>/')
def page(path):
  page = pages.get_or_404(path)
  if 'profiles' in page.path:
    template = page.meta.get('template', 'profile_detail.html')
  else:
    template = page.meta.get('template', 'page.html')
  return render_template(template, page=page)

if __name__ == '__main__':
  app.run(debug=True)