import api

from flask import Flask, render_template, request

app = Flask(__name__)

global_font1 = None
global_font2 = None
g_colors = None


@app.route("/", methods=['GET', 'POST'])
def f():
    global global_font1
    global global_font2
    global g_colors

    if request.method == 'POST':
        c = {}
        x = ['serif', 'sans-serif', 'display', 'handwriting', 'monospace']
        for a in x:
            if request.form['font1'] == a:
                c['font1'] = api.rand_font(a)
            if request.form['font2'] == a:
                c['font2'] = api.rand_font(a)

        if request.form['font1'] == 'lock':
            c['font1'] = global_font1
        else:
            x = api.rand_font()
            c['font1'] = x
            global_font1 = x
        if request.form['font2'] == 'lock':
            c['font2'] = global_font2
        else:
            x = api.rand_font()
            c['font2'] = x
            global_font2 = x

        c['url'] = 'https://fonts.googleapis.com/css?family=' + global_font1 + '|' + global_font2

        colors = ['color0', 'color1', 'color2', 'color3', 'color4']
        new_colors = ['N', 'N', 'N', 'N', 'N']
        for a in range(len(colors)):
            if request.form[colors[a]] == 'lc':
                new_colors[0] = g_colors[a]
            elif request.form[colors[a]] == 'la':
                new_colors[1] = g_colors[a]
            elif request.form[colors[a]] == 'main':
                new_colors[2] = g_colors[a]
            elif request.form[colors[a]] == 'da':
                new_colors[3] = g_colors[a]
            elif request.form[colors[a]] == 'dc':
                new_colors[4] = g_colors[a]

        g_colors = api.colors_request(new_colors)
        hex_colors = api.palett(g_colors)
        c['rgb_colors'] = g_colors
        c['hex_colors'] = hex_colors
        return render_template('home.html', c=c)
    else:
        global_font1 = api.rand_font()
        global_font2 = api.rand_font()
        g_colors = api.colors_request()

        hex_colors = api.palett(g_colors)
        c = {'font1': global_font1,
             'font2': global_font2,
             'url': 'https://fonts.googleapis.com/css?family=' + global_font1 + '|' + global_font2,
             'rgb_colors': g_colors,
             'hex_colors': hex_colors}
        return render_template('home.html', c=c)


