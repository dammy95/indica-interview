"use client"

import Image from "next/image";
import DescriptionIcon from '@mui/icons-material/Description';
import BarChartIcon from '@mui/icons-material/BarChart';
import ShowChartIcon from '@mui/icons-material/ShowChart';
import SecurityIcon from '@mui/icons-material/Security';
import ExploreIcon from '@mui/icons-material/Explore';
import Link from 'next/link'
import { use, useEffect, useState } from "react";


export default function Home() { 
  const imageUrl = "https://eu-assets.simpleview-europe.com/exeter/imageresizer/?image=%2Fdmsimgs%2FEdit_-_For_Great_Hall_-_Piazza_C_University_of_Exeter_944639946.jpg&action=ProductDetailFullWidth2" 
  const [data, setData] = useState({name: '', id: ''});
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/company/home-page-data/')
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
  }, [])

  if (isLoading) return <p className="text-black">Loading...</p>
  if (!data) return <p className="text-black">No company data found</p>

  return (
    <div className="flex flex-row">
      <div className="p-8">
        <Image
          src={imageUrl}
          alt="University of Exeter"
          width={608}
          height={608}
        />
      </div>
      <div className="p-8">
        <div className="flex">
          <ExploreIcon style={{ color: 'black', fontSize: 40 }} />
          <p className="text-black ml-2">{data.name}</p>
        </div>
        <div className="flex">
          <DescriptionIcon style={{ color: 'black', fontSize: 40 }} />
          <Link className="text-black ml-2" href={`/details/${data.id}`}>Details</Link>
        </div>
        <div className="flex">
          <BarChartIcon style={{ color: 'black', fontSize: 40 }} />
          <Link className="text-black ml-2" href={`/measures/${data.id}`}>Measures</Link>
        </div>
        <div className="flex">
          <ShowChartIcon style={{ color: 'black', fontSize: 40 }} />
          <Link className="text-black ml-2" href={`/kpis/${data.id}`}>KPIS</Link>
        </div>
        <div className="flex">
          <SecurityIcon style={{ color: 'black', fontSize: 40 }} />
          <Link className="text-black ml-2" href={`/controls/${data.id}`}>Control</Link>
        </div>
      </div>
    </div>
  );
}
