import logo from './logo.svg';
import './App.css';
import { TodoPage } from './Pages/TodoPage'
import {Show} from './Pages/Show'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Routes
} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route exact path="/" element={<TodoPage />} />
          <Route path="/:id" element={<Show />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
