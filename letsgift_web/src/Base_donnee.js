import axios from "axios";
import React, { useEffect } from "react";

const apiEndPoint = "http://localhost:3004/datas";

const Base_donnee = () => {
  const [datas, setDatas] = useState([]);

  useEffect(() => {
    const updateData = async () => {
      const newPosts = await axios.get(apiEndPoint);
      setDatas(newPosts.data);
    };
    updateData();
  }, []);

  return (
    <div>
      <tbody>
        {data.map((datas) => (
          <tr key={datas.id}>
            <td>{datas.title}</td>
          </tr>
        ))}
      </tbody>
    </div>
  );
};

export default Base_donnee;
