export HOUSE_FINDER_HOME=$HOME/gitsrc/WeChatBot-House-Finder
## start webserver
cd $HOUSE_FINDER_HOME/src/web_server/client
npm install
npm run build
cd $HOUSE_FINDER_HOME/src/web_server/server
npm install
npm start &

## start backendserver
cd $HOUSE_FINDER_HOME/src/backend_server
python service.py &

## start wechatserver
cd $HOUSE_FINDER_HOME/src/wechat_server
python wechat_server.py &

## start pipeline
cd $HOUSE_FINDER_HOME/src/house_listing_pipeline
./house_listing_pipeline_launcher.sh
