def rstudio(context):
  
  MANIFEST = """
  apiVersion: v1
  kind: Pod
  metadata:
    name: rstudio-host
  spec:
    containers:
    - name: rstudio-host
      image: gcr.io/ml-learning-199501/github.com/jasonmhoule/descartes:latest
      imagePullPolicy: Always
      env:
      - name: PASSWORD
        value: {password}
      - name: USER
        value: {user}
      - name: ROOT
        value: true
      - name: SELENIUM_IP
        value: {selenium_ip}
      stdin: true
      tty: true
      ports:
      - containerPort: 8787
        hostPort: 8787
      restartPolicy: Always
  """.format(**context.properties)
  
  return MANIFEST

def selenium():
  
  MANIFEST = """
  apiVersion: v1
  kind: Pod
  metadata:
    name: selenium
  spec:
    containers:
    - name: selenium
      image: docker.io/selenium/standalone-chrome:latest
      imagePullPolicy: Always
      ports:
      - containerPort: 4444
        hostPort: 4444
      restartPolicy: Always
  """
  
  return MANIFEST
