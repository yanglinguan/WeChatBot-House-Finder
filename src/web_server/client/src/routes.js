import Base from './Base/Base';
import App from './App/App';
//import DetailPage from './RequestDetail/DetailPage';
import RequestFormPage from './RequestForm/RequestFormPage';
import HistoryPage from './History/HistoryPage';
import ConfirmationPage from './Confirmation/ConfirmationPage';
import DetailPage from "./Detail/DetailPage";
const routes = {
  component: Base,
  childRoutes: [
    {
      path: '/home/userId/:userId',
      component: App
    },
    {
      path: '/requestForm/userId/:userId', 
      component: RequestFormPage
    },
    {
      path: '/history/userId/:userId',
      component: HistoryPage
    },
    {
      path: '/confirmation/userId/:userId',
      component: ConfirmationPage
    },
    {
      path: '/requestDetail/userId/:userId/requestId/:requestId',
      component: DetailPage
    }
  ]
};

export default routes;

