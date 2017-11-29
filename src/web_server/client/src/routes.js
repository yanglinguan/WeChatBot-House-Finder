import Base from './Base/Base'
import App from './App/App'
//import DetailPage from './RequestDetail/DetailPage';
import RequestFormPage from './RequestForm/RequestFormPage';
import HistoryPage from './History/HistoryPage';

const routes = {
  component: Base,
  childRoutes: [
    {
      path: '/',
      component: App
    },
    {
      path: '/requestForm/userId/:userId', 
      component: RequestFormPage
    },
  //  {
    //  path: 'requestDetail/userId/:userId/requestId/:requestId',
    //  component: DetailPage
  //  },
    {
      path: '/history/userId/:userId',
      component: HistoryPage
    }
  ]
};

export default routes;

