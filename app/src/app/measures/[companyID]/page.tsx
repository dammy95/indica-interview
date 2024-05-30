export default async function Page({ params }: { params: { companyID: string }}) {
    const { companyID } = params;
    const response = await fetch(`http://nginx/api/company/${companyID}/measures/`);
    const errorCode = response.ok ? false : response.status
    const data = await response.json()

    if (errorCode) {
        return <p>Error – could not load company measures page</p>
    }

    console.log({data})

    return (
        <>
            <h2 className="text-black mb-3 text-center">COMPANY MEASURES PAGE</h2>
            <ul>
                {data.map((measure: any) => (
                    <div key={measure.id} className="mb-3">
                        <li className="text-black">Measure Name: {measure.name}</li>
                        <li className="text-black">Measure Value: {measure.value}</li>
                        <li className="text-black">Date recorded: {measure.date_recorded}</li>
                    </div>
                ))}
            </ul>
        </>
    )
}
