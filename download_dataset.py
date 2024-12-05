from roboflow import Roboflow
rf = Roboflow(api_key="your-api-key")
project = rf.workspace("driver-miviz").project("pta-s7fnu-nzeqr")
version = project.version(2)
dataset = version.download("yolov11")