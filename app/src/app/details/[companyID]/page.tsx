export default async function Page({ params }: { params: { companyID: string }}) {
    const { companyID } = params;
    const response = await fetch(`http://nginx/api/company/${companyID}/`);
    const errorCode = response.ok ? false : response.status
    const data = await response.json()

    if (errorCode) {
        return <p>Error – could not load company details page</p>
    }

    return (
        <>
            <h2 className="text-black mb-3 text-center">COMPANY DETAILS PAGE</h2>
            <p className="text-black">Company Name: {data.name}</p>
            <p className="text-black">Description: {data.description}</p>
            <p className="text-black">Founded date: {data.kpis}</p>
            <p className="text-black">Website: {data.kpis}</p>
        </>
    )
}
