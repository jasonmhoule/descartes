def manifest(context):
  
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
  """.format(**context.properties)
  
  return MANIFEST
