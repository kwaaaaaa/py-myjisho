import bookshelf
import config


# Note: debug=True is enabled here to help with troubleshooting. You should
# remove this in production.
app = bookshelf.create_app(config, debug=True)


# Make the queue available at the top-level, this allows you to run
# `psqworker main.books_queue`. We have to use the app's context because
# it contains all the configuration for plugins.
# If you were using another task queue, such as celery or rq, you can use this
# section to configure your queues to work with Flask.
with app.app_context():
    books_queue = bookshelf.tasks.get_books_queue()


# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
