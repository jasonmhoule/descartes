sdriver <- function() {
  
  remoteDriver(remoteServerAddr = Sys.getenv("SELENIUM_IP"),
               port = 4444L,
               browserName = "chrome")
  
}