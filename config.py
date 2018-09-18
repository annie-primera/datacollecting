import os

# Leaving all the comments in because why not?

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'flkjsdfF7348503N=[F-0O3I4URasdfa7U8D54ferP4]WEOIEUPWc45u8O48DHOEkiwerRIGOQ'

# There are three different ways to store the data in the application.
# You can choose 'datastore', 'cloudsql', or 'mongodb'. Be sure to
# configure the respective settings for the one you choose below.
# You do not have to configure the other data backends. If unsure, choose
# 'datastore' as it does not require any additional configuration.
DATA_BACKEND = 'mongodb'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'datacollecting-216815'

# Cloud Datastore dataset id, this is the same as your project id.
DATASTORE_DATASET_ID = PROJECT_ID

# Mongo configuration
# If using mongolab, the connection URI is available from the mongolab control
# panel. If self-hosting on compute engine, replace the values below.
MONGO_URI = 'mongodb://ahibert:stNW65oh@ds259912.mlab.com:59912/datacollection'