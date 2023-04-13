# import os
# from logging import log
#
#
# def startService(self):
#     global haPortNo, haServerSocket
#     log.info("startHA() :: HAgent Started")
#     configURL = os.getenv('configServer')
#     # region = os.getenv('APP_REGION')
#     # country = os.getenv('APP_COUNTRY')
#     hostIPAddr = os.getenv('AgentIp')
#     # node.configUrl = configURL
#     # node.region = region
#     # node.country = country
#     # node.nodeIpAddress = hostIPAddr
#
#
#     while not self.stopService:
#
#         try:
#             ret = node.downloadPropsFromCS()
#
#             if ret == 1:
#                 self.sd = node.loadNodeProperties(self.nodePropFileName)
#                 region = self.sd.region
#                 country = self.sd.country
#                 node.region = region
#                 node.country = country
#                 node.downloadListOfStores(self.storesListFileName)
#                 self.ipWhiteListPattern = fileutil.loadIpWhiteList(self.ipWhitelistFileName)
#
#                 log.info("Node Type: " + self.sd.nodeType)
#                 leaderElection = LeaderElection(self.sd.nodeIpAddress, os.getenv("APP_DB_DIR"))
#             else:
#
#                 logging.error("Could not get Node Properties....")
#             break
#
#         except DMaasException as e:
#             continue
#             log.info("......DMaaS Exception happened and Please Check the Error - INFINITE LOOP")
#             traceback.print_exception(type(e), e, e.__traceback__)
#             continue
#         except Exception as ex:
#             traceback.print_exception(type(ex), ex, ex.__traceback__)
import os
from logging import log
import platform

import self as self

fileName = "IMdbfile.txt"
db_folder = os.getenv("APP_DB_DIR")
dbPath = db_folder + "/" + fileName
if platform.system == 'Windows':
    dbPath.replace("\\", "/")

if not os.path.exists(dbPath):
    try:
        f = open(dbPath, "w")
    except Exception:

        pass

db = InMemoryDB(fileName, db_folder)
db.load1()
log.info("Process Backlog Scheduler started to run every" + str(self.timeDelay) + "Seconds")
shed = BackgroundScheduler(daemon=True)
shed.add_job(lambda: self.processBacklog(), 'interval', seconds=self.timeDelay, max_instances=5000)
shed.start()
shed1 = BackgroundScheduler(daemon=True)
shed1.add_job(lambda: self.monitorHeartBeat(), 'interval', seconds=self.timeDelay)
shed1.start()