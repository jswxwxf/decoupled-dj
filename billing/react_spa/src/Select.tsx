import React from "react";

type Props = {
  id: string;
  name: string;
  options: Array<{
    id: string;
    email: string;
  }>;
};

const Select = ({ id, name, options }: Props) => (
  <select name={name} id={id} required>
    <option value="">---</option>
    {options.map((option) => (
      <option key={option.id} value={option.id}>
        {option.email}
      </option>
    ))}
  </select>
);

export default Select;
