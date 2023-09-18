import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import React from 'react';
import './index.css'
import ListCustomers from './components/pages/ListCustomers';
import CreateCustomerForm from './components/pages/CreateCustomers';

const App = () => {
  
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">List</Link>
            </li>
            <li>
              <Link to="/create">Create</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<ListCustomers />} />
          <Route path="/create" element={<CreateCustomerForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

