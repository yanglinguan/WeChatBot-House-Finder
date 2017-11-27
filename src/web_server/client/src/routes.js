import Base from './Base/Base'
import App from './App/App'
import RequestFormPage from './RequestForm/RequestFormPage';
import HistoryPage from './History/HistoryPage';

const routes = {
  component: Base,
  childRoutes: [
    {
      path: '/requestForm/userId/:userId', 
      component: RequestFormPage
    },
    {
      path: '/history/userId/:userId',
      component: HistoryPage
    }
  ]
};

export default routes;

