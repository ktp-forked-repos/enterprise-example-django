# Token Auth Example - Python Django web app

This example web app demonstrates how developers can integrate GENOME LINK Enterprise API.


## Requirements

- Python >= 3.6
- Django >= 1.11


## How to run

Install required packages.

```bash
$ pip install -r requirements.txt
```

Export `GENOMELINK_CLIENT_ID` and `GENOMELINK_CLIENT_SECRET` as environment variables.

```bash
$ export GENOMELINK_CLIENT_ID=<your_client_id>
$ export GENOMELINK_CLIENT_SECRET=<your_client_secret>
```

Run the app on your localhost.

```bash
$ python manage.py runserver
```

Then, open `http://localhost:8000` in your web browser.


## How it works

By just embedding a tiny HTML tag, you can insert "Connect my DNA" button in your website.

```html
<form action="/" method="POST">
  <script src="https://sdk.genomelink.io/genomelink.js"
          class="genomelink-button"
          data-key="{{ GENOMELINK_CLIENT_ID }}">
  </script>
</form>
```

![screen-shot-01](https://user-images.githubusercontent.com/1478450/38173924-656da8e6-3600-11e8-844f-3a4f5bf51743.png)

When users click the "Connect my DNA" button, a window for registering their DNA will pop up.

![screen-shot-02](https://user-images.githubusercontent.com/1478450/39857476-8358a586-546e-11e8-835f-7ecadd198208.png)

After they successfully upload their data via this window, you will acquire an access token in server-side as POST parameter.

```python
token = request.POST.get('genomelinkToken')
```

This token is issued per user, thus by using this token, you can call the API endpoint for acquiring DNA report of each user from GENOME LINK API server.

![screen-shot-03](https://user-images.githubusercontent.com/1478450/39857481-852103b8-546e-11e8-8f53-728156e6a9a3.png)
