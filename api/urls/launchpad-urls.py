from django.urls import path
from api.controllers.LaunchpadController import getAllLaunchpad

urlpatterns = [
    # Post

    # GET
    path('/get-all', getAllLaunchpad,
         name="propel-pool-get-all"),
]
