export default async function Page({ params }: { params: { companyID: string }}) {
    const { companyID } = params;
    const response = await fetch(`http://nginx/api/company/${companyID}/kpis/`);
    const errorCode = response.ok ? false : response.status
    const data = await response.json()

    if (errorCode) {
        return <p>Error – could not load company KPIS page</p>
    }

    console.log({data})

    return (
        <>
            <h2 className="text-black mb-3 text-center">COMPANY KPIs PAGE</h2>
            <ul>
                {data.map((kpi: any) => (
                    <div key={kpi.id} className="mb-3">
                        <li className="text-black">Name: {kpi.name}</li>
                        <li className="text-black">Target Value: {kpi.target_value}</li>
                        <li className="text-black">Actual Value: {kpi.actual_value}</li>
                        <li className="text-black">Actual Value: {kpi.date_measured}</li>
                    </div>
                ))}
            </ul>
        </>
    )
}
