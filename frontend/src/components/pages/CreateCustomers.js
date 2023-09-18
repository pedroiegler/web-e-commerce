import React, { useState } from "react";
import Swal from 'sweetalert2';

function CreateCustomerForm({ onCustomerCreated }) {
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    date_of_birth: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://localhost:8000/api/customers/create/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        setFormData({
          first_name: "",
          last_name: "",
          date_of_birth: "",
        });
  
        Swal.fire({
          icon: 'success',
          title: 'Cliente criado com sucesso!',
          text: 'O cliente foi criado com sucesso.',
          timer: 3000,
          confirmButtonColor: '#b5102c',
        });
      })
      .catch((error) => {
        console.error("Erro ao criar o Customer:", error);
  
        Swal.fire({
          icon: 'error',
          title: 'Erro ao criar o cliente',
          text: 'Houve um erro ao criar o cliente. Por favor, tente novamente mais tarde.',
        });
      });
  };
  return (
    <div className="container">
      <h1>Criar novo cliente</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <input placeholder="Primeiro nome" type="text" id="first_name" name="first_name" value={formData.first_name} onChange={handleChange} required/>
        </div>
        <div>
          <input placeholder="Sobrenome" type="text" id="last_name" name="last_name"  value={formData.last_name} onChange={handleChange} required/>
        </div>
        <div>
          <label htmlFor="date_of_birth">Data de Nascimento:</label>
          <input type="date" id="date_of_birth" name="date_of_birth" value={formData.date_of_birth} onChange={handleChange}/>
        </div>
        <div>
          <button type="submit">Criar</button>
        </div>
      </form>
    </div>
  );
}

export default CreateCustomerForm;
