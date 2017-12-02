
## start webserver
cd $HOME/gitsrc/WeChatBot-House-Finder/src/web_server/client
npm install
npm run build
cd $HOME/gitsrc/WeChatBot-House-Finder/src/web_server/server
npm install
npm start &

## start backendserver
cd $HOME/gitsrc/WeChatBot-House-Finder/src/backend_server
python service.py &

## start wechatserver
cd $HOME/gitsrc/WeChatBot-House-Finder/src/wechat_server
python wechat_server.py &

## start pipeline
cd $HOME/gitsrc/WeChatBot-House-Finder/src/house_listing_pipeline
./house_listing_pipeline_launcher.sh
