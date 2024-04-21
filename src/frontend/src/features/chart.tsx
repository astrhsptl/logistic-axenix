import { ArcElement, Chart as ChartJS, Legend, Tooltip } from 'chart.js';
import React from 'react';
import { Pie } from 'react-chartjs-2';

interface CategoryData {
  [key: string]: number;
}
interface CharProps {
  data: CategoryData;
}

export const Char: React.FC<CharProps> = ({ data }) => {
  ChartJS.register(ArcElement, Tooltip, Legend);

  const values = {
    labels: Object.keys(data),
    datasets: [
      {
        label: 'Товары',
        data: Object.values(data),
        backgroundColor: [
          'rgba(201, 234, 212, 1)',
          'rgba(103, 197, 135, 1)',
          'rgba(234, 246, 237, 1)',
          'rgba(151, 190, 164, 1)',
          'rgba(178, 255, 204, 1)',
          'rgba(97, 252, 150, 1)',
        ],
        borderColor: [
          'rgba(255, 255, 255, 1)',
          'rgba(255, 255, 255, 1)',
          'rgba(255, 255, 255, 1)',
          'rgba(255, 255, 255, 1)',
          'rgba(255, 255, 255, 1)',
          'rgba(255, 255, 255, 1)',
        ],
        borderWidth: 2,
      },
    ],
  };
  return <Pie data={values} />;
};
