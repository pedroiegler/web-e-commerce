import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import React from 'react';
import ListCustomers from './ListCustomers';
import CreateCustomerForm from './CreateCustomers';

const Header = () => {
  
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

export default Header;

