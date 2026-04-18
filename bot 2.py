2026-04-18T01:29:44.725519796Z ==> Downloading cache...
2026-04-18T01:29:44.761290703Z ==> Cloning from https://github.com/hopps-png/trading-bot
2026-04-18T01:29:44.996867221Z ==> Checking out commit 79df2e85048ec8db33017a563d51e5bb3f26297e in branch main
2026-04-18T01:29:48.646867892Z ==> Downloaded 57MB in 3s. Extraction took 1s.
2026-04-18T01:29:49.794451765Z ==> Using Python version 3.12.11 via environment variable PYTHON_VERSION
2026-04-18T01:29:49.794465875Z ==> Docs on specifying a Python version: https://render.com/docs/python-version
2026-04-18T01:29:49.794603918Z ==> Installing Python version 3.12.11...
2026-04-18T01:30:04.244600549Z ==> Using Poetry version 2.1.3 (default)
2026-04-18T01:30:04.328157779Z ==> Docs on specifying a Poetry version: https://render.com/docs/poetry-version
2026-04-18T01:30:04.408593363Z ==> Running build command 'pip install -r requirements.txt'...
2026-04-18T01:30:04.957129519Z Collecting flask (from -r requirements.txt (line 1))
2026-04-18T01:30:04.958485538Z   Using cached flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
2026-04-18T01:30:04.985950306Z Collecting requests (from -r requirements.txt (line 2))
2026-04-18T01:30:04.987219444Z   Using cached requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
2026-04-18T01:30:05.004611876Z Collecting blinker>=1.9.0 (from flask->-r requirements.txt (line 1))
2026-04-18T01:30:05.007640211Z   Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
2026-04-18T01:30:05.042672702Z Collecting click>=8.1.3 (from flask->-r requirements.txt (line 1))
2026-04-18T01:30:05.042700973Z   Using cached click-8.3.2-py3-none-any.whl.metadata (2.6 kB)
2026-04-18T01:30:05.06030366Z Collecting itsdangerous>=2.2.0 (from flask->-r requirements.txt (line 1))
2026-04-18T01:30:05.061610058Z   Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
2026-04-18T01:30:05.078656373Z Collecting jinja2>=3.1.2 (from flask->-r requirements.txt (line 1))
2026-04-18T01:30:05.079831998Z   Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
2026-04-18T01:30:05.122487522Z Collecting markupsafe>=2.1.1 (from flask->-r requirements.txt (line 1))
2026-04-18T01:30:05.123658688Z   Using cached markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
2026-04-18T01:30:05.144737419Z Collecting werkzeug>=3.1.0 (from flask->-r requirements.txt (line 1))
2026-04-18T01:30:05.145852533Z   Using cached werkzeug-3.1.8-py3-none-any.whl.metadata (4.0 kB)
2026-04-18T01:30:05.234398931Z Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 2))
2026-04-18T01:30:05.235669818Z   Using cached charset_normalizer-3.4.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
2026-04-18T01:30:05.252923798Z Collecting idna<4,>=2.5 (from requests->-r requirements.txt (line 2))
2026-04-18T01:30:05.254007721Z   Using cached idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2026-04-18T01:30:05.279545278Z Collecting urllib3<3,>=1.26 (from requests->-r requirements.txt (line 2))
2026-04-18T01:30:05.280756884Z   Using cached urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
2026-04-18T01:30:05.300657761Z Collecting certifi>=2023.5.7 (from requests->-r requirements.txt (line 2))
2026-04-18T01:30:05.301791245Z   Using cached certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
2026-04-18T01:30:05.311116925Z Using cached flask-3.1.3-py3-none-any.whl (103 kB)
2026-04-18T01:30:05.312463764Z Using cached requests-2.33.1-py3-none-any.whl (64 kB)
2026-04-18T01:30:05.313654179Z Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
2026-04-18T01:30:05.314690711Z Using cached certifi-2026.2.25-py3-none-any.whl (153 kB)
2026-04-18T01:30:05.315910908Z Using cached charset_normalizer-3.4.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (216 kB)
2026-04-18T01:30:05.317095003Z Using cached click-8.3.2-py3-none-any.whl (108 kB)
2026-04-18T01:30:05.318280408Z Using cached idna-3.11-py3-none-any.whl (71 kB)
2026-04-18T01:30:05.319483044Z Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
2026-04-18T01:30:05.320833773Z Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
2026-04-18T01:30:05.322120711Z Using cached markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
2026-04-18T01:30:05.323345837Z Using cached urllib3-2.6.3-py3-none-any.whl (131 kB)
2026-04-18T01:30:05.324559413Z Using cached werkzeug-3.1.8-py3-none-any.whl (226 kB)
2026-04-18T01:30:05.352121544Z Installing collected packages: urllib3, markupsafe, itsdangerous, idna, click, charset_normalizer, certifi, blinker, werkzeug, requests, jinja2, flask
2026-04-18T01:30:06.011691499Z Successfully installed blinker-1.9.0 certifi-2026.2.25 charset_normalizer-3.4.7 click-8.3.2 flask-3.1.3 idna-3.11 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.3 requests-2.33.1 urllib3-2.6.3 werkzeug-3.1.8
2026-04-18T01:30:06.038043833Z 
2026-04-18T01:30:06.038062424Z [notice] A new release of pip is available: 25.0.1 -> 26.0.1
2026-04-18T01:30:06.038067224Z [notice] To update, run: pip install --upgrade pip
2026-04-18T01:30:07.807589426Z ==> Uploading build...
2026-04-18T01:30:12.107838374Z ==> Uploaded in 2.1s. Compression took 2.2s
2026-04-18T01:30:12.177878305Z ==> Build successful 🎉
2026-04-18T01:30:15.010335134Z ==> Deploying...
2026-04-18T01:30:15.131949309Z ==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance
2026-04-18T01:30:41.931975615Z ==> Running 'python bot.py'
2026-04-18T01:30:50.770103047Z  * Serving Flask app 'bot'
2026-04-18T01:30:50.770133658Z  * Debug mode: off
2026-04-18T01:30:50.772710908Z WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
2026-04-18T01:30:50.772726838Z  * Running on all addresses (0.0.0.0)
2026-04-18T01:30:50.772731568Z  * Running on http://127.0.0.1:5000
2026-04-18T01:30:50.772736128Z  * Running on http://10.31.250.184:5000
2026-04-18T01:30:50.77281085Z Press CTRL+C to quit
2026-04-18T01:30:51.808190972Z 127.0.0.1 - - [18/Apr/2026 01:30:51] "HEAD / HTTP/1.1" 404 -
2026-04-18T01:30:54.409470934Z ==> Your service is live 🎉
2026-04-18T01:30:54.554660115Z ==> 
2026-04-18T01:30:54.557050513Z ==> ///////////////////////////////////////////////////////////
2026-04-18T01:30:54.56020953Z ==> 
2026-04-18T01:30:54.562844867Z ==> Available at your primary URL https://trading-bot-umae.onrender.com
2026-04-18T01:30:54.56570129Z ==> 
2026-04-18T01:30:54.568230198Z ==> ///////////////////////////////////////////////////////////
