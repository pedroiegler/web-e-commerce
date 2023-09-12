import React, { useState, useEffect } from "react";
import './styles.css';
import { format } from 'date-fns';

function ListCustomers() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    const loadData = () => {
      fetch("http://localhost:8000/api/customers/")
        .then((response) => response.json())
        .then((data) => setCustomers(data));
    };
    loadData();
  }, []);

  

  return (
    <div className="container">
      <h1>Listagem</h1>

      <table border={1}> 
        <tr className="one">
            <td>Primeiro nome</td>
            <td>Segundo nome</td>
            <td>Data de aniversário</td>
        </tr>
        {customers.map((customer) => (
            <tr key={customer.id}>
                <td>{customer.first_name}</td>
                <td>{customer.last_name}</td>
                <td>{format(new Date(customer.date_of_birth), 'dd/MM/yyyy')}</td>
            </tr>
        ))}
      </table>
    </div>
  );
}

export default ListCustomers;
